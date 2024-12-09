from utils import load_data_from_file

if __name__ == '__main__':

    src = r"E:\A5500\LLaVA-Med\answer_output\answer-file.jsonl"
    data = load_data_from_file(src)
    print(data)