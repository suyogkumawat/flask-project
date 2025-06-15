from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Project Showcase</title>
        <style>
            header {
                background-color: #ff0000; /* Customize with your channel's color */
                color: #ffffff;
                text-align: center;
                padding: 2rem;
            }
            /* Reset some default styles */
            body, h1, p {
                margin: 0;
                padding: 0;
            }

            /* Set a background color or image */
            body {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
            }

            /* Center align content */
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                text-align: center;
            }

            .video-container, .playlist-container, .shorts-container {
                display: flex;
                justify-content: center;
                gap: 1rem;
            }

            .video, .playlist, .short {
                flex: 1;
                border: 1px solid #ddd;
                padding: 1rem;
                background-color: #ffffff;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            /* Footer section */
            footer {
                text-align: center;
                padding: 1rem;
                background-color: #333;
                color: #ffffff;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Flask app on ECS</h1>
            <p class="channel-description">Welcome to my channel! Subscribe for awesome content.</p>
        </header>
        <div class="container">
            <h1>Popular Videos</h1>
            <br>
            <!-- Popular YouTube Videos -->
            <div class="video-container">
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/" frameborder="0" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Popular YouTube Playlists -->
            <br>
            <h1>Popular Playlists</h1>
            <br>
            <div class="playlist-container">
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/yaml-and-industry-based-scenarios-67e63249b245" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/ultimate-guide-crack-the-aws-certified-solutions-architect-associate-exam-in-2025-78fb1a4bf19b" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="video">
                    <iframe width="560" height="315" src="https://guideclouddevops.medium.com/yaml-and-industry-based-scenarios-67e63249b245" frameborder="0" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Popular YouTube Shorts -->
            <br>
            <h1>Popular Shorts</h1>
            <br>
            <div class="shorts-container">
                <div class="short">
                    <iframe width="315" height="560" src="https://guideclouddevops.medium.com/" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="short">
                    <iframe width="315" height="560" src="https://guideclouddevops.medium.com/" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="short">
                    <iframe width="315" height="560" src="https://guideclouddevops.medium.com/eks-auto-mode-new-feature-aws-0603a8c78797" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="short">
                    <iframe width="315" height="560" src="https://guideclouddevops.medium.com/eks-auto-mode-new-feature-aws-0603a8c78797" frameborder="0" allowfullscreen></iframe>
                </div>
                <div class="short">
                    <iframe width="315" height="560" src="https://guideclouddevops.medium.com/eks-auto-mode-new-feature-aws-0603a8c78797" frameborder="0" allowfullscreen></iframe>
                </div>
            </div>
        </div>
        <footer>
            © 2024 GuideCloudDevOps | All rights reserved
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
