from flask import Flask
from flask import render_template
from flask import request
import math


app = Flask("forces on vehicles")

@app.route("/")
def search():
    return render_template("home.html")


@app.route("/home",methods=["GET"])
def cal():
    roll_coeff = float(request.args.get("x1"))
    kerb_weight = float(request.args.get("x2"))
    person_weight = float(request.args.get("x3"))
    density = float(request.args.get("x4"))
    width = float(request.args.get("x5"))
    height = float(request.args.get("x6"))
    velocity = float(request.args.get("x7"))
    drag_coeff = float(request.args.get("x8"))
    angle_of_gredability = float(request.args.get("x9"))
    final_angle = float(angle_of_gredability*0.0174533)
    gravitaional_force = 9.81
    rolling_resistance_force= roll_coeff*(kerb_weight+person_weight)*gravitaional_force
    z1 = int(rolling_resistance_force)
    aero_dynamic_force = 0.5*density*width*height*drag_coeff*(velocity/3.6)**2
    z2 = int(aero_dynamic_force)
    hill_climbimg_force = (kerb_weight+person_weight)*gravitaional_force*math.sin(math.radians(final_angle))
    z3 = int(hill_climbimg_force)
    p1 = float(rolling_resistance_force)
    p2 = float(aero_dynamic_force)
    p3 = float(hill_climbimg_force)
    Total_power = ((p3+p2+p1)*(velocity/3.6)*0.001)
    z4 = int(Total_power)
    return render_template("result.html",k1=z1,k2=z2,k3=z3,k4=z4)




