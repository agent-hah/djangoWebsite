from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
posts: list[dict[str, str | int]] = [
    {
        "id": 0,
        "title": "let's explore python",
        "content": "python is a great language to learn for beginners and professionals alike. It is versatile and can be used for web development, data analysis, machine learning, and more.",
    },
    {
        "id": 1,
        "title": "let's explore django",
        "content": "django is a high-level python web framework that encourages rapid development and clean, pragmatic design. It is built by experienced developers and takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.",
    },
    {
        "id": 2,
        "title": "let's explore react",
        "content": "react is a javascript library for building user interfaces. It is maintained by facebook and a community of individual developers and companies. React can be used as a base in the development of single-page or mobile applications.",
    },
]


def home(_request: HttpRequest) -> HttpResponse:
    html: str = ""
    for post in posts:
        html += f"""
            <div>
                <a href="/post/{post["id"]}/">
                    <h1>{post["id"]} - {post["title"]}</h1>
                </a>
                <p>{post["content"]}</p>
            </div>
    """
    return HttpResponse(html)


def redirectToHome(_request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(reverse("home"))


def postDetail(_request: HttpRequest, id: int) -> HttpResponseNotFound | HttpResponse:
    html: str = ""
    for post in posts:
        if post["id"] == id:
            html += f"""
                <div>
                    <h1>{post["title"]}</h1>
                    <p>{post["content"]}</p>
                </div>
            """
    if html == "":
        html += "<h1>Post not found</h1>"
        html += f"<a href={reverse('home')}>Go back to home page</a>"
        return HttpResponseNotFound(html)
    else:
        html += f"<a href={reverse('home')}>Go back to home page</a>"
        return HttpResponse(html)


def google(_request: HttpRequest, id: int) -> HttpResponseRedirect:
    return HttpResponseRedirect(reverse("post", args=[id]))
