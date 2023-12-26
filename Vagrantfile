Vagrant.configure("2") do |config|
#nginx-loadbalancer
  config.vm.define "webserver" do |node1|
    node1.vm.box = "ubuntu/trusty64"
    
    node1.vm.network "public_network", bridge: "eno1", ip: "192.168.0.17"
    node1.vm.network "forwarded_port", guest: 22, host: 2221, host_ip: "127.0.0.1"
 
    
    node1.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end
    node1.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/nginx-playbook.yml" # Replace with your actual playbook
      ansible.inventory_path = "inventory.ini" # Replace with your #inventory path
    end
  end

#App-server
  config.vm.define "appserver" do |node2|
    node2.vm.box = "ubuntu/trusty64"
    # Private Network Configuration
    node2.vm.network :private_network, ip: "192.168.57.7"
    node2.vm.network "forwarded_port", guest: 22, host: 2202, host_ip: "127.0.0.1"
    
    node2.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 1
    end
    node2.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/appserver.yml" # Replace with your actual playbook
      ansible.inventory_path = "inventory.ini" # Replace with your inventory path
    end
  end

#Mysql-database-server  
  config.vm.define "database-server" do |node3|
    node3.vm.box = "ubuntu/trusty64"
    # Private Network Configuration
    node3.vm.network :private_network, ip: "192.168.58.4"
    node3.vm.network "forwarded_port", guest: 22, host: 2226,	host_ip: "127.0.0.1"
    
    node3.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 1
    end
    node3.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/database.yml" # Replace with your database playbook
      ansible.inventory_path = "inventory.ini" # Replace with your inventory path
    end
  end
end
