# -*- coding: utf-8 -*-
## $Id$

## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005 CERN.
##
## The CDSware is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## The CDSware is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDSware; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


def format(bfo, style):
    """
    Prints a link to BibEdit, if authorization is granted

    @param style the CSS style to be applied to the link.
    """
    from invenio.config import weburl
    from invenio.webuser import getUid
    from invenio.access_control_engine import acc_authorize_action
    
    out = ""
    
    uid = bfo.uid
    if uid != None:
        (auth_code, auth_message) = acc_authorize_action(uid,'runbibedit')
        if auth_code == 0:
            print_style = ''
            if style != '':
                print_style = 'style="' + style + '"'
            
            out += '<a href="'+weburl + '/admin/bibedit/bibeditadmin.py/index?recid=' + str(bfo.recID) +'" ' + print_style + '>Edit This Record</a>'
            
    return out