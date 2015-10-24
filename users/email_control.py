import mandrill
from django.conf import settings



mandrill_client = mandrill.Mandrill(settings.MAINDRILL_API)


def welcome_email(email,username):
     '''
     Send welcome email using mandrill api and template.
     To change template go to mandrill and alter the welcome template
     :param email:
     :param password:
     :return:
     '''

     template_content = [{'uname': 'example content', 'password': 'welcome'}]

     message = {
          'from_email': 'info@asylguiden.se',
          'from_name': 'Asylguiden',
          'auto_html':True,
          'auto_text':True,
          "global_merge_vars": [
               {
                    "name": "username",
                    "content": username
               },
               ],
          'important': True,
          'metadata': {'website': 'asylguiden.se'},
          'subject': 'Welcome to Asylguiden.se',
          'tags': ['welcome'],
          'merge': True,
          'merge_language': 'handlebars',
          'to': [{'email': email,
             'type': 'to'}]}
     manddrill_result = mandrill_client.messages.send_template(template_name='welcome_to_Asylguiden', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
     for r in manddrill_result:
          if r['status'] =="sent":
               '''
               Messige send sucess
               '''
               return True
          else:
               '''
               Something went wrong in the email return false
               '''
               print('Error sending welcome email to '+email)
               return False

def lost_password(email,username,password):
     '''
     Send welcome email using mandrill api and template.
     To change template go to mandrill and alter the welcome template
     :param email:
     :param password:
     :return:
     '''

     template_content = [{'uname': 'example content', 'password': 'welcome'}]

     message = {
          'from_email': 'info@asylguiden.se',
          'from_name': 'Asylguiden',
          'auto_html':True,
          'auto_text':True,
          "global_merge_vars": [
               {
                    "name": "username",
                    "content": username
               },
                              {
                    "name": "password",
                    "content": password
               },
               ],
          'important': True,
          'metadata': {'website': 'asylguiden.se'},
          'subject': 'Welcome to Asylguiden.se',
          'tags': ['welcome'],
          'merge': True,
          'merge_language': 'handlebars',
          'to': [{'email': email,
             'type': 'to'}]}
     manddrill_result = mandrill_client.messages.send_template(template_name='welcome_to_Asylguiden', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
     for r in manddrill_result:
          if r['status'] =="sent":
               '''
               Messige send sucess
               '''
               return True
          else:
               '''
               Something went wrong in the email return false
               '''
               print('Error sending welcome email to '+email)
               return False
