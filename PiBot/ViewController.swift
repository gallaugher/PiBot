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
    
    let mqttClient = CocoaMQTT(clientID: "PiBotApp", host: "pibot", port: 1883)
    // let mqttClient = CocoaMQTT(clientID: "PiBotApp", host: "10.0.1.32", port: 1883)
    
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

