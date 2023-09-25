Vagrant.configure("2") do |config|

  # Define the Kubernetes nodes
  config.vm.define "master" do |master|
    master.vm.box = "bento/ubuntu-22.04"
    master.vm.hostname = "master"
    master.vm.network "public_network", bridge: "enp2s0"
    master.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
    end
  end
end