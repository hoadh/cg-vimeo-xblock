"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblockutils.studio_editable import StudioEditableXBlockMixin

class CGVimeoXBlock(StudioEditableXBlockMixin, XBlock):

    vimeo_id = String(
        default="351106148",
        scope=Scope.content,
        help="Vimeo ID",
    )

    editable_fields = ('vimeo_id', 'display_name')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the CGVimeoXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/cgvimeo.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/cgvimeo.css"))
        frag.add_javascript(self.resource_string("static/js/src/cgvimeo.js"))
        frag.initialize_js('CGVimeoXBlock')
        return frag

    @XBlock.json_handler
    def get_vimeo_id(self, data, suffix=''):
        return {"vimeo_id": self.vimeo_id}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("CGVimeoXBlock",
             """<cgvimeo/>
             """),
            ("Multiple CGVimeoXBlock",
             """<vertical_demo>
                <cgvimeo/>
                <cgvimeo/>
                <cgvimeo/>
                </vertical_demo>
             """),
        ]
