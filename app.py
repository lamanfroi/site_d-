from flask import Flask, Response, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/robots.txt")
def robots():
    return Response(
        "User-agent: *\nAllow: /\n\nSitemap: https://oraculodode.com.br/sitemap.xml\n",
        mimetype="text/plain",
    )


@app.route("/sitemap.xml")
def sitemap():
    return Response(
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
        "<url><loc>https://oraculodode.com.br/</loc></url>"
        "</urlset>",
        mimetype="application/xml",
    )


if __name__ == "__main__":
    app.run(debug=False)