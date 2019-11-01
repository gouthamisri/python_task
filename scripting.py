from fpdf import FPDF
name=raw_input("please enter your name")
age=raw_input("please enter your age")
phnumber=raw_input("please enter your phone number")
city=raw_input("please enter your city name")

data={"name":name,"age":age,"phnumber":phnumber,"city":city}
user_choice=raw_input("please enter your choice text/pdf")
if user_choice == "text":
    with open("userdata.txt","w+") as f:
        for i in data:
            f.write(i+":"+"{}".format(data[i]) +'\n')
elif user_choice == "pdf":
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    for i in data:
        pdf.cell(0, 10, txt=i+":"+"{}".format(data[i]), ln=1, align="L")
    pdf.output('test.pdf', 'F')
