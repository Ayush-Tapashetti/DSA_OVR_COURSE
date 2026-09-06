

class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = homepage
        print(f" Opened browser at: {self.current_page}")

    def visit(self, url):
        # 1. Save the current page to the back history
        self.back_stack.append(self.current_page)
        
        # 2. Go to the new page
        self.current_page = url
        
        # 3. Visiting a new page always clears the forward history!
        self.forward_stack.clear()
        
        print(f" Visited: {self.current_page}")

    def back(self):
        if not self.back_stack:
            print(" Can't go back. History is empty.")
            return self.current_page
            
        # Save the current page to forward history before leaving it
        self.forward_stack.append(self.current_page)
        
        # Pop the last visited page from the back stack
        self.current_page = self.back_stack.pop()
        
        print(f"  Went back to: {self.current_page}")
        return self.current_page

    def forward(self):
        if not self.forward_stack:
            print(" Can't go forward. Forward history is empty.")
            return self.current_page
            
        # Save the current page to back history before leaving it
        self.back_stack.append(self.current_page)
        
        # Pop the next page from the forward stack
        self.current_page = self.forward_stack.pop()
        
        print(f"  Went forward to: {self.current_page}")
        return self.current_page


# Testing the Browser History
if __name__ == "__main__":
    browser = BrowserHistory("google.com")
    
    # User browses some pages
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    browser.visit("python.org")
    
    print("\n Testing Navigation ")
    browser.back()      
    browser.back()      
    browser.forward()   

    print("\n Testing New Visit Override ")
    browser.visit("wikipedia.org")
    browser.forward()   