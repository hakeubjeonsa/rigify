import bpy


class BaseRig(object):

    def __init__(self, obj, bone_name, params):
        """
        Rig Base class the bones struct is a dict with 'org' as a list and 'def' 'mch' and 'ctrl' dicts
        ctrls mchs and defs must be organized in groups. If your Rig Class has just one group you can call it all_ctrls
        :param obj:
        :param bone_name:
        :param params:
        """

        self.obj = obj
        self.params = params
        self.bones = dict()
        self.bones['org'] = [bone_name]
        self.base_bone = bone_name

        # Get all the recursive ORG children of the base bone BUT the rig_type trees
        for edit_bone in self.obj.data.edit_bones[bone_name].children:
            if self.obj.pose.bones[edit_bone.name].rigify_type != "":
                continue
            else:
                self.bones['org'].append(edit_bone.name)
            for child in edit_bone.children_recursive:
                self.bones['org'].append(child.name)

        self.bones['ctrl'] = dict()
        self.bones['mch'] = dict()
        self.bones['def'] = dict()

    def create_mch(self):
        pass

    def create_def(self):
        pass

    def create_controls(self):
        pass

    def create_widgets(self):
        pass

    def make_constraints(self):
        pass

    def parent_bones(self):
        pass

    def generate(self):
        pass