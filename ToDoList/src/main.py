import Task
import TaskList
import IOFunctions


def main():
    IOFunctions.write_list(
            TaskList.add_task(
                IOFunctions.read_list(),
                Task.create_task(
                    IOFunctions.get_name_input(),
                    IOFunctions.get_date_input()
                    )
                )
            )
    IOFunctions.print_task_list(IOFunctions.read_list())


if __name__ == "__main__":
    main()
