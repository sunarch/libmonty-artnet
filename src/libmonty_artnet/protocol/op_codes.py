#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# This is an ArtPoll packet,
# no other data is contained in this UDP packet.
OpPoll = 0x2000

# This is an ArtPollReply Packet.
# It contains device status information.
OpPollReply = 0x2100

# Diagnostics and data logging packet.
OpDiagData = 0x2300

# Used to send text based parameter commands.
OpCommand = 0x2400

# This is an ArtDmx data packet.
# It contains zero start code DMX512 information for a single Universe.
OpOutput = 0x5000
OpDmx = 0x5000

# This is an ArtNzs data packet.
# It contains non-zero start code (except RDM) DMX512 information
# for a single Universe.
OpNzs = 0x5100

# This is an ArtSync data packet.
# It is used to force synchronous transfer of ArtDmx packets
# to a node’s output.
OpSync = 0x5200

# This is an ArtAddress packet.
# It contains remote programming information for a Node.
OpAddress = 0x6000

# This is an ArtInput packet.
# It contains enable – disable data for DMX inputs.
OpInput = 0x7000

# This is an ArtTodRequest packet.
# It is used to request a Table of Devices (ToD) for RDM discovery.
OpTodRequest = 0x8000

# This is an ArtTodData packet.
# It is used to send a Table of Devices (ToD) for RDM discovery.
OpTodData = 0x8100

# This is an ArtTodControl packet.
# It is used to send RDM discovery control messages.
OpTodControl = 0x8200

# This is an ArtRdm packet.
# It is used to send all non discovery RDM messages.
OpRdm = 0x8300

# This is an ArtRdmSub packet.
# It is used to send compressed, RDM Sub-Device data.
OpRdmSub = 0x8400

# This is an ArtVideoSetup packet.
# It contains video screen setup information for nodes that implement
# the extended video features.
OpVideoSetup = 0xa010

# This is an ArtVideoPalette packet.
# It contains colour palette setup information for nodes that implement
# the extended video features.
OpVideoPalette = 0xa020

# This is an ArtVideoData packet.
# It contains display data for nodes that implement
# the extended video features.
OpVideoData = 0xa040

# This packet is deprecated.
OpMacMaster = 0xf000

# This packet is deprecated.
OpMacSlave = 0xf100

# This is an ArtFirmwareMaster packet.
# It is used to upload new firmware or firmware extensions
# to the Node.
OpFirmwareMaster = 0xf200

# This is an ArtFirmwareReply packet.
# It is returned by the node to acknowledge receipt
# of an ArtFirmwareMaster packet or ArtFileTnMaster packet.
OpFirmwareReply = 0xf300

# Uploads user file to node.
OpFileTnMaster = 0xf400

# Downloads user file from node.
OpFileFnMaster = 0xf500

# Server to Node acknowledge for download packets.
OpFileFnReply = 0xf600

# This is an ArtIpProg packet.
# It is used to re-programme the IP address and Mask of the Node.
OpIpProg = 0xf800

# This is an ArtIpProgReply packet.
# It is returned by the node to acknowledge receipt
# of an ArtIpProg packet.
OpIpProgReply = 0xf900

# This is an ArtMedia packet.
# It is Unicast by a Media Server and acted upon by a Controller.
OpMedia = 0x9000

# This is an ArtMediaPatch packet.
# It is Unicast by a Controller and acted upon by a Media Server.
OpMediaPatch = 0x9100

# This is an ArtMediaControl packet.
# It is Unicast by a Controller and acted upon by a Media Server.
OpMediaControl = 0x9200

# This is an ArtMediaControlReply packet.
# It is Unicast by a Media Server and acted upon by a Controller.
OpMediaContrlReply = 0x9300

# This is an ArtTimeCode packet.
# It is used to transport time code over the network.
OpTimeCode = 0x9700

# Used to synchronise real time date and clock
OpTimeSync = 0x9800

# Used to send trigger macros
OpTrigger = 0x9900

# Requests a node's file list
OpDirectory = 0x9a00

# Replies to OpDirectory with file list
OpDirectoryReply = 0x9b00
