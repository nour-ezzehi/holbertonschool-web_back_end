export default class Curreency {
  constructor(code, name) {
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) !== 'string') throw new TypeError('Name must be a string');
    else this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof (code) !== 'string') throw new TypeError('Code must be a string');
    else this._code = code;
  }

  displayFullCurrency() {
    return (`${this.name} (${this.code})`);
  }
}
