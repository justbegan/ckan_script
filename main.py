
from deepdiff import DeepDiff
# from datetime import datetime
# from multiprocessing import current_process
import multiprocessing
import argparse
import logging

from services.get_query_from_db_by_id import get_report_by_id, get_geo_by_id
from services.update import Update
from services.get_data_from_api import get_reports, get_geo
from services.mail_sender import send_email


file_log = logging.FileHandler("logfile.log")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.DEBUG)


class Main():
    def __init__(self, process_count: int, geo: bool) -> None:
        """
        Args:
            process_count (int): Количество процессов
            geo (bool): Если флага geo нет то запуститься report по умолчанию
        """
        self.process_count = process_count
        self.geo = geo

    def start(self):
        """
        Запуск
        """
        try:
            logging.info("script start")
            result_queue = multiprocessing.Queue()
            for i in self.get_task():
                p = multiprocessing.Process(target=self.manager, args=(i, result_queue))
                p.start()
            logging.info("script completed successfully")
        except Exception as e:
            send_email(e)
            logging.error(e)

    def get_task(self) -> list:
        """Разделяет список задач на количество процессов

        Returns:
            list: Возврашаяет список данных разделенный на количество процессов
        """
        if not self.geo:
            my_list = get_reports()
        else:
            my_list = get_geo()

        avg = len(my_list) / float(self.process_count)
        tasks = []
        last = 0.0
        while last < len(my_list):
            tasks.append(my_list[int(last):int(last + avg)])
            last += avg
        return tasks

    def manager(self, data: list, result_queue):
        """Менеджер, Следить за рабочим процессом

        Args:
            data (list): список заданий
            result_queue (_type_): _description_
        """
        # x = datetime.now()
        # print(f"{current_process().name} start")
        processed_data = self.worker(data)
        result_queue.put(processed_data)
        # print(f"{current_process().name} complited {datetime.now() - x}")

    def worker(self, worker_task_list: list):
        """Рабочий, делает всю работу

        Args:
            worker_task_list (list): списой заданий
        """
        for i in worker_task_list:
            if not self.geo:
                x = get_report_by_id(i['id'])
            else:
                x = get_geo_by_id(i['id'])
            diff = DeepDiff(i, x)
            if diff:
                print(diff)
                u = Update(i, self.geo)
                u.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Синхронизация ckan')
    parser.add_argument('--p', type=int, help='Количество процессов')
    parser.add_argument('--geo', action='store_true', help='Режим синхронизации гео данных')
    args = parser.parse_args()
    geo = args.geo
    process_count = args.p

    if process_count is not None:
        m = Main(process_count, geo)
        m.start()
    else:
        raise Exception("flag --p required")
