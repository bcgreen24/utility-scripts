from gi.repository import Gtk
from xml.etree import ElementTree as ET
#import lxml.etree as etree

root = ET.Element("beans")
print type(root)
print type(ET)
dictCourseList = {}

class Crops_Config:
    
    #def prettyPrintET(self, etNode):
        #reader = Sax2.Reader()
        #docNode = reader.fromString(ET.tostring(etNode))
        #tmpStream = StringIO()
        #PrettyPrint(docNode, stream=tmpStream)
        #return tmpStream.getvalue()

    def prettify(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.prettify(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        return elem

    def build_file(self, root):
        bean = ET.SubElement(root, "bean")
        bean.attrib["id"] = txtBeanID.get_text()
        bean.attrib["class"] = "edu.ucmerced.banner.api.BannerSiteInstructions"
        bean.attrib["parent"] = "customCourseSiteDefaults"
        if chkTesting.get_active() == 1:
            theproperty = ET.SubElement(bean, "property")
            theproperty.attrib["name"] = "testing"
            theproperty.attrib["value"] = "true"
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "custom"
        theproperty.attrib["value"] = "true"
        #term code
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "termCode"
        theproperty.attrib["value"] = txtTermCode.get_text()
        #site id
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "siteId"
        theproperty.attrib["value"] = '${termcode}-' + txtSiteID.get_text()
        #site title
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "siteTitle"
        theproperty.attrib["value"] = '${semestercode}-' + txtSiteTitle.get_text()
        #short description
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "shortDescription"
        theproperty.attrib["value"] = txtSiteDescription.get_text()
        #emailAlias
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "emailAlias"
        theproperty.attrib["value"] = '${semestercode}-' + txtSiteID.get_text()
        #section name
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "sectionName"
        theproperty.attrib["value"] = '${subjectcode}-${coursenumber}-${sectiontypedesc}-${sectionid}'
        theproperty = ET.SubElement(bean, "property")
        theproperty.attrib["name"] = "sections"
        thelist = ET.SubElement(theproperty, "list")
        #loop through sections and add them  
        for key, value in dictCourseList.iteritems():
            thevalue = ET.SubElement(thelist, "value")
            thevalue.text = 'subjcode=' + key + ',crsenumb=' + value
        return root

    def exitProgram(self, *args):
        Gtk.main_quit(*args)
    
    def on_btnAddCourse_released(self, *args):
        strSubjCode = txtSubjCode.get_text()
        strCourseNum = txtCourseNum.get_text()
        buff = txtCourseList.get_buffer()
        buff.set_text('Subject Code: ' + strSubjCode + ' - Course Number: ' + strCourseNum)
        dictCourseList[strSubjCode] = strCourseNum
        
    def on_btnWrite_released(self, *args):
        global root
        root.clear()
        root = ET.Element("beans")
        self.build_file(root)
        self.prettify(root)
        ET.ElementTree(root).write("course.xml")
    
    #def tree_to_text(self, *args):
         #fileHandle = open("~/course.xml", "r")
         #tree = etree.parse(fileHandle)
         #return etree.tostring(tree, pretty_print=True)
             
    def on_btnPreview_released(self, *args):
        global root
        root.clear()
        root = ET.Element("beans")
        self.build_file(root)
        buff = txtPreview.get_buffer()
        self.prettify(root)
        #ET.ElementTree(root).write("~/course.xml")
        #buff.set_text(self.tree_to_text)
        ET.dump(root)

    def on_btnCopySiteID_released(self, *args):
        txtBeanID.set_text(txtSiteID.get_text())
        txtBeanID.set_text(txtSiteID.get_text())
        txtSiteTitle.set_text(txtSiteID.get_text())
        txtSiteDescription.set_text(txtSiteID.get_text())
        txtEmailAlias.set_text(txtSiteID.get_text())
    
    def on_btnClearAll_released(self, *args):
        txtSiteID.set_text("")
        txtSubjCode.set_text("")
        txtCourseNum.set_text("")
        txtBeanID.set_text("")
        txtTermCode.set_text("")
        txtSiteTitle.set_text("")
        txtSiteDescription.set_text("")
        txtEmailAlias.set_text("")

builder = Gtk.Builder()
builder.add_from_file("merge_crops_sites.glade")
builder.connect_signals(Crops_Config())
window = builder.get_object("WindowMain")
txtSiteID = builder.get_object("txtSiteID")
txtCourseList = builder.get_object("txtCourseList")
txtSubjCode = builder.get_object("txtSubjCode")
txtCourseNum = builder.get_object("txtCourseNum")
txtPreview = builder.get_object("txtPreview")
txtBeanID = builder.get_object("txtBeanID")
txtTermCode = builder.get_object("txtTermCode")
txtSiteTitle = builder.get_object("txtSiteTitle")
txtSiteDescription = builder.get_object("txtSiteDescription")
chkTesting = builder.get_object("chkTesting")
btnCopySiteID = builder.get_object("btnCopySiteID")
btnClearAll = builder.get_object("btnClearAll")
txtEmailAlias = builder.get_object("txtEmailAlias")
window.show_all()

Gtk.main()
