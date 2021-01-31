import yaml


def getYmal():
    with open('data/cal.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print(data['idsAdd'])
        return data


if __name__ == '__main__':
    getYmal()