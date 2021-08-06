class BlogPost:
    _observers = []

    def __init__(self) -> None:
        self.likes = 0

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def like(self) -> None:
        self.likes += 1
        self.notify()


class LikesObserver:
    def update(self, blog_post):
        if blog_post.likes == 5:
            print(
                f"LikesObserver: {blog_post.likes} likes!",
                "Moving BlogPost to the Top!"
                )
        elif blog_post.likes < 5:
            print(f"LikesObserver: Not enough likes: {blog_post.likes}... Skip")

if __name__ == "__main__":
    blog_post = BlogPost()
    observer = LikesObserver()
    blog_post.attach(observer)

    for _ in range(10):
        blog_post.like()