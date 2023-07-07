#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Op codes
"""

# This is an ArtPoll packet,
# no other data is contained in this UDP packet.
OP_POLL: int = 0x2000

# This is an ArtPollReply Packet.
# It contains device status information.
OP_POLL_REPLY: int = 0x2100

# Diagnostics and data logging packet.
OP_DIAG_DATA: int = 0x2300

# Used to send text based parameter commands.
OP_COMMAND: int = 0x2400

# This is an ArtDmx data packet.
# It contains zero start code DMX512 information for a single Universe.
OP_OUTPUT: int = 0x5000
OP_DMX: int = 0x5000

# This is an ArtNzs data packet.
# It contains non-zero start code (except RDM) DMX512 information
# for a single Universe.
OP_NZS: int = 0x5100

# This is an ArtSync data packet.
# It is used to force synchronous transfer of ArtDmx packets
# to a node’s output.
OP_SYNC: int = 0x5200

# This is an ArtAddress packet.
# It contains remote programming information for a Node.
OP_ADDRESS: int = 0x6000

# This is an ArtInput packet.
# It contains enable – disable data for DMX inputs.
OP_INPUT: int = 0x7000

# This is an ArtTodRequest packet.
# It is used to request a Table of Devices (ToD) for RDM discovery.
OP_TOD_REQUEST: int = 0x8000

# This is an ArtTodData packet.
# It is used to send a Table of Devices (ToD) for RDM discovery.
OP_TOD_DATA: int = 0x8100

# This is an ArtTodControl packet.
# It is used to send RDM discovery control messages.
OP_TOD_CONTROL: int = 0x8200

# This is an ArtRdm packet.
# It is used to send all non discovery RDM messages.
OP_RDM: int = 0x8300

# This is an ArtRdmSub packet.
# It is used to send compressed, RDM Sub-Device data.
OP_RDM_SUB: int = 0x8400

# This is an ArtVideoSetup packet.
# It contains video screen setup information for nodes that implement
# the extended video features.
OP_VIDEO_SETUP: int = 0xa010

# This is an ArtVideoPalette packet.
# It contains colour palette setup information for nodes that implement
# the extended video features.
OP_VIDEO_PALETTE: int = 0xa020

# This is an ArtVideoData packet.
# It contains display data for nodes that implement
# the extended video features.
OP_VIDEO_DATA: int = 0xa040

# This packet is deprecated.
OP_MAC_MASTER: int = 0xf000

# This packet is deprecated.
OP_MAC_SLAVE: int = 0xf100

# This is an ArtFirmwareMaster packet.
# It is used to upload new firmware or firmware extensions
# to the Node.
OP_FIRMWARE_MASTER: int = 0xf200

# This is an ArtFirmwareReply packet.
# It is returned by the node to acknowledge receipt
# of an ArtFirmwareMaster packet or ArtFileTnMaster packet.
OP_FIRMWARE_REPLY: int = 0xf300

# Uploads user file to node.
OP_FILE_TN_MASTER: int = 0xf400

# Downloads user file from node.
OP_FILE_FN_MASTER: int = 0xf500

# Server to Node acknowledge for download packets.
OP_FILE_FN_REPLY: int = 0xf600

# This is an ArtIpProg packet.
# It is used to re-programme the IP address and Mask of the Node.
OP_IP_PROG: int = 0xf800

# This is an ArtIpProgReply packet.
# It is returned by the node to acknowledge receipt
# of an ArtIpProg packet.
OP_IP_PROG_REPLY: int = 0xf900

# This is an ArtMedia packet.
# It is Unicast by a Media Server and acted upon by a Controller.
OP_MEDIA: int = 0x9000

# This is an ArtMediaPatch packet.
# It is Unicast by a Controller and acted upon by a Media Server.
OP_MEDIA_PATCH: int = 0x9100

# This is an ArtMediaControl packet.
# It is Unicast by a Controller and acted upon by a Media Server.
OP_MEDIA_CONTROL: int = 0x9200

# This is an ArtMediaControlReply packet.
# It is Unicast by a Media Server and acted upon by a Controller.
OP_MEDIA_CONTROL_REPLY: int = 0x9300

# This is an ArtTimeCode packet.
# It is used to transport time code over the network.
OP_TIME_CODE: int = 0x9700

# Used to synchronise real time date and clock
OP_TIME_SYNC: int = 0x9800

# Used to send trigger macros
OP_TRIGGER: int = 0x9900

# Requests a node's file list
OP_DIRECTORY: int = 0x9a00

# Replies to OpDirectory with file list
OP_DIRECTORY_REPLY: int = 0x9b00
