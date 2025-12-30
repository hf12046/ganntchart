def create_gantt_chart(df):
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    return fig

def main():
    data = {
        "Task": ["Project A", "Project B", "Project C", "Project D", "Project E"],
        "Start": [
            datetime.datetime(2023, 1, 1),
            datetime.datetime(2023, 1, 15),
            datetime.datetime(2023, 2, 1),
            datetime.datetime(2023, 2, 10),
        ],
        "Finish": [
            datetime.datetime(2023, 1, 20),
            datetime.datetime(2023, 2, 5),
            datetime.datetime(2023, 2, 20),
            datetime.datetime(2023, 3, 1),
        ],
        "Resource": ["Team 1", "Team 2", "Team 1", "Team 3"],
    }
    df = pd.DataFrame(data)

    fig = create_gantt_chart(df)
    fig.show()

if __name__ == "__main__":
    main()