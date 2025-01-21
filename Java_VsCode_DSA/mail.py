import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl

# List of HR email addresses
hr_emails = [
"sumitkumar070465@gmail.com",
"rahulgupta1012.rk@gmail.com",
"akanksha.puri@sourcefuse.com",
"akanksha.sogani@perennialsys.com",
"akhil@ibhubs.co",
"akhila@estuate.com",
"akram.mohammad@colruytgroup.com",
"akriti@elsner.in",
"akshata.bhandare@windmill.ch",
"albino@pixis.ai",
"allwyn.r@qbrainx.com",
"alok.singh@recro.io",
"alok.kumar@vfislk.com",
"alwyn.barretto@infrasoftech.com",
"aman.khan@areteanstech.com",
"amandeep.k@antiersolutions.com",
"amar.sinha@nitorinfotech.com",
"ambrish.kanungo@beyondkey.com",
"amit.avasthi@altudo.com",
"amit.malhotra@wundermanthompson.com",
"amit@hanu.com",
"amit.prayagi@claimgenius.com",
"amit.ranjan@scikey.ai",
"amit.sahoo@areteanstech.com",
"ashital@svam.com",
"amitesh.verma@cheersin.com",
"amitha.k@secure-24.com",
"amlesh.nag@murugappa.com",
"amreshm@zendrive.com",
"akishore@dimagi.com",
"amrita.cheema@loconav.com",
"amrita.singh@cogentinfo.com",
"amrita.singh@itbd.net",
"amrita@sdanaglobal.com",
"amritesh.shukla@mygate.com",
"amruta@greatplaceitservices.com",
"amulya.ms@uthunga.com",
"anand.christopher@grassrootsbpo.com",
"anand.e@increff.com",
"ak@8kmiles.com",
"anandk@pharmarack.com",
"anand.r@whatarage.com",
"anand@hubilo.com",
"anand@auzmor.com",
"anand@capsitech.com",
"athiagarajan@inniveninc.com",
"anandhi.s@dsmsoft.com",
"ananthram.iyer@customercentria.com",
"anrastogi@enhanceit.com",
"aarasina@teksystems.com",
"angel.mathew@delphix.com",
"anil.chandra@thoughtspot.com",
"anil.k@corestack.io",
"anil.moturi@solugenix.com",
"anil.pereira@visiblealpha.com",
"anil.kumar@flytxt.com",
"anil.tomar@fddsolutions.com",
"animesh.kumar@novopay.in",
"anindita.ranjan@d3s.ai",
"anirban.chakravorty@nttdata.com",
"aghosh@trimaxamericas.com",
"anirudh.vasudevan@replicon.com",
"anish.ahmed@vaave.com",
"anish.raj@sentieo.com",
"anita.chakravarty@capricot.com",
"anoronha@shorewise.com",
"asidhwani@cleo.com",
"anita.yadav@appventurez.com",
"anitha.davis@incture.com",
"anitha.prabhakar@pramati.com",
"anjali.g@knackforge.com",
"anjali.g@mangoapps.com",
"anjali.patil@workindia.in",
"anjali.sharma@fulcrumdigital.com",
"anjan.bose@hpl.co.in",
"anjan.sailan@h.nibssap.com",
"anju.tyagi@bpoconvergence.com",
"ankit@computantrice.com",
"ankit.sharma@a1technology.com",
"ankit.tomar@rategain.com",
"ankita@zenwork.com",
"ankita.rajrishi@condecosoftware.com",
"ankita.sinha@mtxb2b.com",
"ankur.beri@niit-tech.com",
"ankur.dewan@smartek21.com",
"anna@transactglobal.com",
"anne.manoj@fime.com",
"anoop.abraham@arcadia.com",
"anshika.khatan@getvymo.com",
"ansuman.s@mindfiresolutions.com",
"anshuman@absolutdata.com",
"anubhav.sahu@urbanladder.com",
"anuj@deskera.com",
"anuj.sivaram@convance.com",
"anupam.j@gs.in",
"anupam.srivastava@reltio.com",
"anupama@eremax.com",
"anupriya.gandhi@juliacomputing.com",
"anurag.rana@sironlabs.com",
"anurag.s@talisma.com",
"anurag.verma@uniphore.com",
"anusha.kishore@loco.gg",
"anusha.jayachandran@srstechsolutions.com",
"anusha.jayachandran@somnium.com"
]

# Your email credentials
your_email = "sumitkumar808393@gmail.com"
your_password = " "  # Use an app-specific password

# Email subject and body template
subject = "Application for Data Analyst Role"
message_body = """
Dear HR,

I hope this email finds you well. I am writing to express my interest in the Data Analyst position at your company. I have attached my resume for your review and would be grateful for the opportunity to discuss how my skills and experiences align with your team’s needs.

Thank you for considering my application. I look forward to the possibility of contributing to your esteemed organization.

Best regards,
Sumit
"""

# Path to your resume
resume_path = r"D:\Java Program\Java_VsCode_DSA\Sumit Resume New.pdf"

def send_email(to_email):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(message_body, 'plain'))

        # Attach the resume
        with open(resume_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="Sumit Kumar Resume.pdf"'
        )
        msg.attach(part)

        # Send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(your_email, your_password)
            server.sendmail(your_email, to_email, msg.as_string())

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Send emails to all HR contacts
for email in hr_emails:
    send_email(email)
