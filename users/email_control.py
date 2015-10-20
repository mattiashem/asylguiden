import mandrill
from settings import mandrill_client



#mandrill_client = mandrill.Mandrill('API KEY')


def welcome_email(email,password):
     '''
     Send welcome email using mandrill api and template.
     To change template go to mandrill and alter the welcome template
     :param email:
     :param password:
     :return:
     '''

     template_content = [{'uname': 'example content', 'password': 'welcome'}]

     message = {
          'from_email': 'team@samma.io',
          'from_name': 'The Samma.io Team',
          'auto_html':True,
          'auto_text':True,
          "global_merge_vars": [
               {
                    "name": "uname",
                    "content": email
               },
              {
                    "name": "pass",
                    "content": password
               }
               ],
          'important': True,
          'metadata': {'website': 'samma.io'},
          'subject': 'Welcome to Samma.io',
          'tags': ['welcome'],
          'merge': True,
          'merge_language': 'handlebars',
          'to': [{'email': email,
             'type': 'to'}]}
     manddrill_result = mandrill_client.messages.send_template(template_name='welcome', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
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





def newpassword_email(email,password):
     '''
     Send new password email using mandrill api and template.
     To change template go to mandrill and alter the newpassword template
     :param email:
     :param password:
     :return:
     '''

     template_content = [{'uname': 'example content', 'password': 'welcome'}]

     message = {
          'from_email': 'team@samma.io',
          'from_name': 'The Samma.io Team',
          'auto_html':True,
          'auto_text':True,
          "global_merge_vars": [
               {
                    "name": "uname",
                    "content": email
               },
              {
                    "name": "pass",
                    "content": password
               }
               ],
          'important': True,
          'metadata': {'website': 'samma.io'},
          'subject': 'New password for Samma.io',
          'tags': ['newpass'],
          'merge': True,
          'merge_language': 'handlebars',
          'to': [{'email': email,
             'type': 'to'}]}
     manddrill_result = mandrill_client.messages.send_template(template_name='newpass', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
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
               print('Error sending newpass email to '+email)
               return False





def baseline_alert(email,domain,content):
     '''
     Send welcome email using mandrill api and template.
     To change template go to mandrill and alter the welcome template
     :param email:
     :param password:
     :return:
     '''

     template_content = [{'uname': 'example content', 'password': 'welcome'}]

     message = {
          'from_email': 'team@samma.io',
          'from_name': 'The Samma.io Team',
          'auto_html':True,
          'auto_text':True,
          "global_merge_vars": [
               {
                    "name": "content",
                    "content": content
               },
              {
                    "name": "domain",
                    "content": domain
               }
               ],
          'important': True,
          'metadata': {'website': 'samma.io'},
          'subject': 'Alert from Samma.io '+domain+' has changed',
          'tags': ['basline_alert'],
          'merge': True,
          'merge_language': 'handlebars',
          'to': [{'email': email,
             'type': 'to'}]}
     manddrill_result = mandrill_client.messages.send_template(template_name='baseline_alert', template_content=template_content, message=message, async=False, ip_pool='Main Pool')
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
               print('Error sending baseline email to '+email)
               return False
