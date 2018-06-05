var eventBus = function(eventbus) {
  var eventbus = eventbus;

  return {
    on: function(name,cb) {
      eventbus.addEventListener(name, cb);
    },
    trigger: function(name, data) {
      var event = new Event(name);
      event.data = data;
      eventbus.dispatchEvent(event);
    }
  };
};
