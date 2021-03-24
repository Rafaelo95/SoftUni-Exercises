from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.john = Student('John', {'Algebra': [6]})
        self.amy = Student('Amy', None)

    def test_if_init_is_properly_initialized(self):
        self.assertEqual(self.john.name, 'John')
        self.assertEqual(self.amy.name, 'Amy')
        self.assertEqual(self.john.courses, {'Algebra': [6]})
        self.assertEqual(self.amy.courses, {})

    def test_if_enroll_appends_correctly_if_course_name_exists_in_courses(self):
        actual = self.john.enroll('Algebra', ['good', 5])
        expected_result = {'Algebra': [6, 'good', 5]}
        expected_message = "Course already added. Notes have been updated."
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.john.courses, expected_result)

    def test_if_course_notes_are_Y(self):
        expected_message = "Course and course notes have been added."
        actual_with_y = self.amy.enroll('Biology', [1, 2, 3], 'Y')
        expected_result = self.amy.courses['Biology'] = [1, 2, 3]
        self.assertEqual(actual_with_y, expected_message)
        self.assertEqual(self.amy.courses['Biology'], expected_result)

    def test_if_course_notes_are_empty_string(self):
        expected_message = "Course and course notes have been added."
        actual = self.amy.enroll('Biology', [1, 2, 3])
        expected_result = self.amy.courses['Biology'] = [1, 2, 3]
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.amy.courses['Biology'], expected_result)

    def test_if_enroll_creates_a_new_list_if_course_name_does_not_exist(self):
        actual = self.john.enroll('Biology', [1, 2, 3], 'Not Y or empty')
        expected_message = "Course has been added."
        expected_result = {'Algebra': [6], 'Biology': []}
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.john.courses, expected_result)

    def test_add_notes_method_if_course_name_is_found(self):
        actual = self.john.add_notes('Algebra', [5, 5, 'great'])
        expected_message = "Notes have been updated"
        expected_result = self.john.courses['Algebra'] = [6, 5, 5, 'great']
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.john.courses['Algebra'], expected_result)

    def test_add_notes_method_if_course_name_cannot_be_found(self):
        with self.assertRaises(Exception) as context_manager:
            self.john.add_notes('Biology', [1])
        expected_result = "Cannot add notes. Course not found."
        self.assertEqual(str(context_manager.exception), expected_result)

    def test_leave_course_method_if_course_name_exists(self):
        self.john = Student('John', {'Algebra': [6], 'Biology': [5]})
        actual = self.john.leave_course('Algebra')
        expected_message = "Course has been removed"
        expected_result = {'Biology': [5]}
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.john.courses, expected_result)

    def test_leave_course_method_if_course_does_not_exist(self):
        with self.assertRaises(Exception) as context_manager:
            self.amy.leave_course('Algebra')
        expected_message = "Cannot remove course. Course not found."
        self.assertEqual(str(context_manager.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
