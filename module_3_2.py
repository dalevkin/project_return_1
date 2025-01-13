
def send_email(message, recipient, sender="university.help@gmail.com"):
    if validate_email(recipient) != True or validate_email(sender) != True:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif recipient == sender:
        print(f'Невозможно отправить письмо самому себе')
    elif sender!="university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


def validate_email(email_address_param):
    if '@' not in email_address_param:
        return False
    if '.com' not in email_address_param and '.ru' not in email_address_param and '.net' not in email_address_param:
        return False

    return True


if __name__ == '__main__':
    #---------------------------------------------------
    print(f'Случай 1: Стандартный sender. Recipient не содержит @ и не в зоне ru,com или net')
    recipient_address = 'test_address_gmail.org'
    send_email('Пожалуйста, исправьте задание', recipient_address)
    # ---------------------------------------------------
    print(f'Случай 2: Стандартный sender. Recipient не содержит @')
    recipient_address = 'test_address_gmail.com'
    send_email('Пожалуйста, исправьте задание',recipient_address)
    # ---------------------------------------------------
    print(f'Случай 3: Стандартный sender. Recipient содержит @, но не в зоне ru,com или net')
    recipient_address = 'test_address@gmail.org'
    send_email('Пожалуйста, исправьте задание', recipient_address)
    # ---------------------------------------------------
    print(f'Случай 4: Стандартный sender. Recipient содержит @ и в зоне ru,com или net')
    recipient_address = 'test_address@gmail.com'
    send_email('Пожалуйста, исправьте задание', recipient_address)
    # ---------------------------------------------------
    print(f'Случай 5: Нестандартный sender: test_address@gmail.com. Recipient содержит @ и в зоне ru,com или net')
    recipient_address = 'test_sender@gmail.com'
    send_email('Пожалуйста, исправьте задание', recipient_address,'test_address@gmail.com')
    # ---------------------------------------------------
    print(f'Случай 5: Нестандартный sender: test_address@gmail.com. Recipient содержит @ и в зоне ru,com или net. Sender=Recipient')
    recipient_address = 'test_address@gmail.com'
    send_email('Пожалуйста, исправьте задание', recipient_address,'test_address@gmail.com')