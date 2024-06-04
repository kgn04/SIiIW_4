import matplotlib.pyplot as plt


def print_values_distribution(columns: list[dict]) -> None:
    for column in columns:
        print(column['name'])
        for key in column:
            if key != 'name':
                print(f'\t{key}: {column[key]}')


def visualise_values_distribution(columns: list[dict]) -> None:
    for column in columns:
        column_name = column['name']
        values = [key for key in column if key != 'name']
        counts = [column[key] for key in column if key != 'name']

        sorted_items = sorted(zip(values, counts), key=lambda x: x[1], reverse=True)
        sorted_values, sorted_counts = zip(*sorted_items)

        plt.figure(figsize=(10, 5))
        bars = plt.bar(sorted_values, sorted_counts, color='lightgreen')
        plt.title(f'Value Distribution in {column_name}')
        plt.xlabel('Value')
        plt.ylabel('Count')

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()


def visualise_rows_distribution(rows: dict[str, int]) -> None:
    repeats_count = {
        '1-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0,
        '51-60': 0,
        '61-70': 0,
        '71-80': 0,
        '81-90': 0,
        '91-100': 0,
        '101-110': 0,
        '111-120': 0,
        '121-130': 0,
        '131-140': 0
    }
    for scope in repeats_count:
        l, r = scope.split('-')
        l, r = int(l), int(r)
        for count in rows.values():
            if l <= count <= r:
                repeats_count[scope] += 1
    plt.figure(figsize=(10, 5))
    bars = plt.bar(list(repeats_count.keys()), list(repeats_count.values()), color='lightgreen')
    plt.title(f'Rows repetition Distribution')
    plt.xlabel('Row repeats')
    plt.ylabel('Count')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, int(yval), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    columns = []
    lines = {}
    with open('data.csv') as data:
        for i, line in enumerate(data):
            try:
                lines[line] += 1
            except KeyError:
                lines[line] = 1
            for j, value in enumerate(line[:-1].split(',')):
                if i == 0:
                    columns.append({'name': value})
                elif value not in columns[j]:
                    columns[j][value] = 1
                else:
                    columns[j][value] += 1

    # print_values_distribution(columns)
    # visualise_values_distribution(columns)
    visualise_rows_distribution(dict(sorted(lines.items(), key=lambda item: item[1])))
    print(dict(sorted(lines.items(), key=lambda item: item[1])))
