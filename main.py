import os
from pydicom import dcmread

PATH = './src'


def data_transformation(fds):
    """
    Анонимизирует файлы. Создает для файлов директории и переименовывает,
    используя значения ключей:
    $StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm
    """

    for cdm in fds:
        with open(f'{PATH}/{cdm}', 'rb') as infile:
            ds = dcmread(infile)
            ds.PatientName = None
            dir_1 = ds.StudyInstanceUID
            dir_2 = ds.SeriesInstanceUID
            name_cdm = ds.SOPInstanceUID
            file_path = f'{dir_1}/{dir_2}/{name_cdm}.cdm'
            # if
            os.makedirs(f'{dir_1}/{dir_2}/', exist_ok=True)

            rec_path_changes(cdm, file_path)

            ds.save_as(file_path)


def rec_path_changes(path, new_path):
    """
    Записывает старый и новый путь к файлу cdm в файл txt.
    """

    with open('logs_of_file_path_changes.txt', 'a') as f:
        f.write(f'{PATH}/{path} ===========> {new_path}')


if __name__ == '__main__':
    fds = sorted(os.listdir(PATH))
    data_transformation(fds)
