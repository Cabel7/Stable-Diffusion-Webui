import json
import os
from modules import shared, ui_extra_networks


class ExtraNetworksPageHypernetworks(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('Hypernetwork')

    def refresh(self):
        shared.reload_hypernetworks()

    def list_items(self):
        for name, path in shared.hypernetworks.items():
            fn = os.path.splitext(path)[0]
            name = os.path.relpath(fn, shared.opts.hypernetwork_dir)
            yield {
                "type": 'Hypernetwork',
                "name": os.path.relpath(fn, shared.opts.hypernetwork_dir),
                "filename": path,
                "preview": self.find_preview(fn),
                "description": self.find_description(fn),
                "info": self.find_info(fn),
                "search_term": self.search_terms_from_path(name),
                "prompt": json.dumps(f"<hypernet:{name}:{shared.opts.extra_networks_default_multiplier}>"),
                "local_preview": f"{fn}.{shared.opts.samples_format}",
            }

    def allowed_directories_for_previews(self):
        return [shared.opts.hypernetwork_dir]
