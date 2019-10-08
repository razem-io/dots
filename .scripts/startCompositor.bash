#!/bin/bash

killall compton || true
compton --backend glx
