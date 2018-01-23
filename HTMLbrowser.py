from HTMLparser import HTMLparser
from request_utils import get_page_text
from request_utils import InvalidURL
from tkinter_utils import EntryLabelFrame
from tkinter import Tk, Button, Listbox
from tkinter import messagebox
from tkinter import END

ALL = "NSEW"


def check_parser(func):
    def wrapper(obj, *args, **kwargs):
        if not obj.parser.is_set():
            messagebox.showerror('Error', 'You must fetch a URL first.')
        return func(obj, *args, **kwargs)
    return wrapper


class HTMLbrowser(Tk):

    def __init__(self):
        # Window
        super().__init__()
        self.option_readfile('style.txt')
        self.title('HTML Browser')
        self.resizable(0, 0)

        # HTMLparser
        self.parser = HTMLparser()

        # Widgets
        self.url_frame = EntryLabelFrame(self, 'URL: ')
        self.url_frame.grid(row=0, column=0)
        self.fetch_button = Button(self, text='Fetch url', command=self.get_url)
        self.fetch_button.grid(row=1, column=0)

        self.listbox = Listbox(self, width=100)
        self.listbox.grid(row=2, column=0)
        self.tags_button = Button(self, text='Get tags', command=self.show_available_tags)
        self.tags_button.grid(row=3, column=0)

        self.pattern_frame = EntryLabelFrame(self, 'Pattern: ')
        self.pattern_frame.grid(row=4, column=0)
        self.select_button = Button(self, text='Get matches', command=self.show_pattern_matches)
        self.select_button.grid(row=5, column=0)

        # Common grid formatting
        for child in self.winfo_children():
            child.grid(columnspan=2, sticky=ALL)

    def get_url(self):
        try:
            self.parser.set_html(get_page_text(self.url_frame.get()))
        except InvalidURL as error:
            messagebox.showerror('Error', error.message)
        self.fetch_button.config(background='green')

    def update_listbox(self, values):
        self.listbox.delete(0, END)
        for value in values:
            self.listbox.insert(END, value)

    @check_parser
    def show_available_tags(self):
        tags_list = self.parser.get_available_tags()
        self.update_listbox(tags_list)

    @check_parser
    def show_pattern_matches(self):
        pattern = self.pattern_frame.get()
        matches_list = self.parser.get_pattern_matches(pattern)
        self.update_listbox(matches_list)


if __name__ == '__main__':
    HTMLbrowser().mainloop()
