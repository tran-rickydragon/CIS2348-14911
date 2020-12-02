""""Ricky Tran - 1832920"""


def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age):
    fbhr = (220 - age) * 0.7
    return fbhr


if __name__ == "__main__":
    try:
        age = get_age()
        hr = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', hr, 'bpm')
    except ValueError as ve:
        print(ve)
        print('Could not calculate heart rate info.\n')
