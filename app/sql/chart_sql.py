from .config import connection
# from config import connection
def count_phone_number(phoneNumber):
    cursor = connection.cursor()

    # Query number of occurrences in the 'spam' table
    query_spam = "SELECT COUNT(*) FROM spam WHERE phoneNumber = %s"
    cursor.execute(query_spam, (phoneNumber,))
    number_in_spam = cursor.fetchone()[0]  # fetchone() returns a tuple

    # Query number of occurrences in the 'inbox' table
    query_inbox = "SELECT COUNT(*) FROM inbox WHERE phoneNumber = %s"
    cursor.execute(query_inbox, (phoneNumber,))
    number_in_inbox = cursor.fetchone()[0]

    connection.commit()
    cursor.close()

    return number_in_spam, number_in_inbox