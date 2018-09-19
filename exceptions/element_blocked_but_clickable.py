from selenium.common.exceptions import WebDriverException


class ElementBlockedButClickableException(WebDriverException):
    message = 'This exception raises when element was clickable but click on him has been failed'
