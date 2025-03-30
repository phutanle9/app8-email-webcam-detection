import smtplib, ssl
from email.message import EmailMessage
import mimetypes

SENDER = "phutanle912@gmail.com"
RECEIVER = "phutanle912@gmail.com"
PASSWORD = "teodnwfysinzupjs"

def send_email(image_path):
    try:
        print("send mail started")

        email_message = EmailMessage()
        email_message["Subject"] = ("New customer showed up!")
        email_message.set_content("Hey, we just saw a new customer!")

        # Get the MIME type of the image
        mime_type, _ = mimetypes.guess_type(image_path)
        if mime_type is None:
            print("Could not determine MIME type of the file.")
            return

        main_type, sub_type = mime_type.split("/")

        with open(image_path, "rb") as file:
            content = file.read()
        email_message.add_attachment(content, maintype=main_type, subtype=sub_type)

        # Connect to Gmail SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
            gmail.ehlo()  # Greet the server
            gmail.starttls()  # Start TLS encryption
            gmail.login(SENDER, PASSWORD)
            gmail.sendmail(SENDER, RECEIVER, email_message.as_string())

        print("Email sent end")

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email(image_path="images/19.png")
