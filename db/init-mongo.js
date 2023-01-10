db = new Mongo().getDB("forms_db");
db.createCollection('forms', { capped: false });
const fs = require('fs')
const data = JSON.parse(fs.readFileSync('/docker-entrypoint-initdb.d/forms.json', 'utf-8'))
db.forms.insert(data)
