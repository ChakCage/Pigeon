from database import get_connection


class TaskRepository:

    def get_all(self, is_completed=None):
        connection = get_connection()
        cursor = connection.cursor()

        if is_completed is None:
            cursor.execute(
                """
                SELECT * FROM tasks
                ORDER BY id;
                """
            )
        else:
            cursor.execute(
                """
                SELECT * FROM tasks
                WHERE is_completed = %s
                ORDER BY id;
                """,
                (is_completed,)
            )

        tasks = cursor.fetchall()

        cursor.close()
        connection.close()

        return tasks

    def create(self, title, description=None):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (title, description)
            VALUES (%s, %s)
            RETURNING *;
            """,
            (title, description)
        )

        task = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return task

    def get_by_id(self, task_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM tasks
            WHERE id = %s;
            """,
            (task_id,)
        )

        task = cursor.fetchone()

        cursor.close()
        connection.close()

        return task

    def update(self, task_id, title, description, is_completed):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = %s,
                description = %s,
                is_completed = %s
            WHERE id = %s
            RETURNING *;
            """,
            (title, description, is_completed, task_id)
        )

        task = cursor.fetchone()

        connection.commit()
        cursor.close()
        connection.close()

        return task

    def delete(self, task_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = %s
            RETURNING *;
            """,
            (task_id,)
        )
        task = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return task