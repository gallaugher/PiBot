//
//  ViewController.swift
//  PiBot
//
//  Created by John Gallaugher on 2/9/19.
//  Copyright © 2019 John Gallaugher. All rights reserved.
//

import UIKit
import CocoaMQTT

class ViewController: UIViewController {

    var stop = "stop"
    var direction: [Int: String] = [0: "forward",
                                    1: "backward",
                                    2: "left",
                                    3: "right"]
    
    // *** IMPORTANT NOTE: Make sure your host name is entered properly, below ***
    let mqttClient = CocoaMQTT(clientID: "PiBotApp", host: "pibot.local", port: 1883)
    // let mqttClient = CocoaMQTT(clientID: "PiBotApp", host: "zerobot.local", port: 1883)
    // If you still have problems, make sure spelling is exactly as you've named your Pi
    // and is what you use when you ssh log in.
    // If that still doesn't work, try removing .local from the name.
    // And if that still doesn't work, try putting your Pi's IP address in between the quotes
    // instead of pibot.local.
    // ** REMEMBER: You'll have to click the "Play" Build/Run button in the upper left corner
    // each time you modify this code, so that you're running the code with your latest changes.
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func buttonDown(_ sender: UIButton) {
        print("Sending message: \(direction[sender.tag]!)")
        mqttClient.publish("pibot/move", withString: direction[sender.tag]!)
    }
    
    
    @IBAction func buttonUp(_ sender: UIButton) {
        print("Sending message: \(stop)")
        mqttClient.publish("pibot/move", withString: stop)
    }
    

    @IBAction func connectButtonPressed(_ sender: UIButton) {
        mqttClient.connect()
    }
    
}

