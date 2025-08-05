# Basic Ansible Project Structure
- inventory.ini
- site.yml
- roles/common/tasks/main.yml
- roles/webserver/tasks/main.yml
- roles/webserver/templates/nginx.conf.j2
- roles/webserver/handlers/main.yml
- roles/database/tasks/main.yml
- ansible.cfg

## I've created a practical Ansible project structure that includes:
1. Inventory File (inventory.ini):
- Defines server groups (webservers and databases)
- Uses localhost for practice purposes

2. Main Playbook (site.yml):
- Orchestrates the entire configuration
- Applies roles to specific server groups

3. Roles:
- common: Basic system configuration
- webserver: Nginx installation and configuration
- database: PostgreSQL setup

4. Configuration (ansible.cfg):
- Basic Ansible configuration settings

## To use this setup:
1. Run the entire playbook:
```
ansible-playbook site.yml
```

1. Run the entire playbook:
```
ansible-playbook site.yml
```

2. Run for specific hosts:
```
ansible-playbook site.yml --limit webservers
```

3. Run with check mode (dry run):
```
ansible-playbook site.yml --check
```

## This example demonstrates Ansible best practices:
- Role-based organization
- Handlers for service management
- Templates for configuration files
- Variables and conditionals
- Separate responsibilities into distinct roles
- Modular and reusable components
