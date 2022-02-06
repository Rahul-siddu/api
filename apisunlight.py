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
           {"company":"tcs","place":"mumbai","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]},
           {"company":"goldmansach","place":"bangalore","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]},
           {"company":"zensor technology","place":"kolkata","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]},
           {"company":"wipro","place":"hyderabad","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]}]}
    b=json.dumps(a,indent=5)
    return b
if __name__=='__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')
    
