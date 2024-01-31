import chromedriver_autoinstaller


def print_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@print_function_call
def closeCards(cardsClosebtns):
    for btn in cardsClosebtns:
        btn.click()


@print_function_call
def getvoteBtns(VoteParents):
    VoteBtns = []
    for btn in VoteParents:
        VoteBtns.append(btn)
    return VoteBtns


@print_function_call
def get_chrome_browser_version():
    dpath = chromedriver_autoinstaller.install(path="assets")
    print(dpath)
    chrome_browser_version = chromedriver_autoinstaller.get_chrome_version()

    return chrome_browser_version
