import os
from flask import Flask, request, jsonify, render_template_string
from googlesearch import search
import time
domain = 'google.com'
subdomains = set()


app = Flask(__name__)

# import datetime

# host = www.{A..Z*}.google.com
# while True:
#     result = os.system("ping", host)

#     if result == 0:
#         Print("subdomains are up")
#     else:
#         Please check

@app.route('/')
def hello():
    return "hello"

@app.route('/dashboard', methods= ['GET', 'POST'])    
def route():
    while True:
        for result in search(f'site:*.{domain}', num_results=100):  # searching the ggogle engine for subdomain with domains
    # print (result)
            subdomain = result.split('/')[2].split('.')[0]   # splitting the result first on // and then on . to fetch the o index value for subdoamin
            subdomains.add(subdomain)  # using set for uniq values for subdomain
        results = {}
        for subdomain in sorted(subdomains): 
            result = os.system(f'ping -n 1 {subdomain}.{domain}') #checking availability of url 
            if result == 0:
                status = 'up'
                results[f'{subdomain}.{domain}'] = status  # appending to dictionary result diclared
            else:
                status = 'down'
                results[f'{subdomain}.{domain}'] = status
        # table_template = """

        # <table>
        #     <tr>
        #         <th>Subdomains</th>
        #         <th>Status</th>
        #     </tr>
        #     {% for subdomain, status in results.items() %}
        #         <tr>
        #             <td>{{ subdomain }}</td>
        #             <td>{{ status }}</td>
        #         </tr>
        #     {% endfor %}
        # </table>
        # """
        # rendered_table = render_template_string(table_template, results=results)
        time.sleep(60)
        return results
        # return rendered_table
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)