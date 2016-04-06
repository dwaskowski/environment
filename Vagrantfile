Vagrant.configure("2") do |config|
  config.vm.box = "debian/jessie64"
  config.vm.hostname = "dev-global-docker"
  config.vm.provision :shell, path: "bootstrap.sh"

  config.vm.network :private_network, ip: "192.168.255.38"
  config.vm.synced_folder "./www", "/srv/www", :nfs => true
  config.vm.synced_folder "./docker", "/docker", :nfs => true
end