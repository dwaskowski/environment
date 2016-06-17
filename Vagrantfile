Vagrant.configure("2") do |config|
  config.vm.box = "debian/jessie64"
  config.vm.hostname = "dev-docker"
  config.vm.boot_timeout = 300

  config.vm.provision :shell, path: "bootstrap.sh"

  config.vm.network :private_network, ip: "192.168.255.38"

  config.ssh.forward_agent = true

  config.vm.synced_folder "./www", "/srv/www", :nfs => true
  config.vm.synced_folder "./docker", "/docker", :nfs => true

  config.vm.provider :virtualbox do |vb|
    vb.name = "DevDockerBox"
    vb.customize [
      "modifyvm", :id,
      "--memory", 8192,
      "--cpus", 2
    ]
  end  
end
