from flask import Flask
import json
import os
app=Flask(__name__)
@app.route('/api')
def webhook():
    a={"list":[{"company":"sunlight","place":"delhi","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]},
           {"company":"tcs","place":"mumbai","employee details":[{"name":"rahul siddu","state":"telangana"},
                                                                {"name":"suresh kumar gupta","state":"maharastra"},
                                                                {"name":"shanthanu","state":"gujarat"},
                                                                {"name":"srivatsav","state":"delhi"},
                                                                {"name":"krishna","state":"us"}]},
           {"company":"goldmansach","place":"bangalore","employee details":[{"name":"dravid","state":"telangana"},
                                                                {"name":"pavan","state":"maharastra"},
                                                                {"name":"ritesh","state":"gujarat"},
                                                                {"name":"vijay","state":"delhi"},
                                                                {"name":"kris","state":"us"}]},
           {"company":"zensor technology","place":"kolkata","employee details":[{"name":"nimesh","state":"telangana"},
                                                                {"name":"srinivas","state":"maharastra"},
                                                                {"name":"arjun","state":"gujarat"},
                                                                {"name":"naryana","state":"delhi"},
                                                                {"name":"immanuel","state":"us"}]},
           {"company":"wipro","place":"hyderabad","employee details":[{"name":"quareshi","state":"telangana"},
                                                                {"name":"praneeth","state":"maharastra"},
                                                                {"name":"dinesh","state":"gujarat"},
                                                                {"name":"bala krishna","state":"delhi"},
                                                                {"name":"rohith","state":"us"}]}]}
    b=json.dumps(a,indent=5)
    return b
if __name__=='__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')
    
