from seedbox.config_renderer.ignition.base import BaseIgnitionPackage


class KubeProxyPackage(BaseIgnitionPackage):
    def __init__(self, hyperkube_tag, apiserver_endpoint, set_kubeconfig):
        self.template_context = {
            'hyperkube_tag': hyperkube_tag,
            'apiserver_endpoint': apiserver_endpoint,
            'set_kubeconfig': set_kubeconfig,
        }

    def get_files(self):
        return [
            {
                'filesystem': 'root',
                'path': '/etc/kubernetes/manifests/kube-proxy.yaml',
                'mode': 0o644,
                'contents': {
                    'source': self.to_data_url(self.render_template('manifest.yaml')),
                },
            },
        ]