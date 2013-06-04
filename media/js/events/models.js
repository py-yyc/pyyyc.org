define(['jquery'], function($) {
	var Venue = function(obj) {
		var self = this;
		var obj = obj || {};
		self.address = $.grep([
		    obj.address_1 || '',
		    obj.address_2 || ''
		], function(element) { return element !== '' });
		self.city = obj.city;
		self.state = obj.state;
		self.lat = obj.lat;
		self.lon = obj.lon;
		self.name = obj.name;

		self.toString = function() {
			return self.name + "<br/>" + self.address.join("<br/>") + "<br/>" +
			[self.city, self.state].join("<br/>");
		};
	};

	var Event = function(obj) {
		var self = this;
		var obj = obj || {};
		self.announced = obj.announced;
		self.created = obj.created;
		self.description = obj.description;
		self.event_url = obj.event_url;
		self.id = obj.id;
		self.headcount = obj.headcount;
		self.name = obj.name;
		self.rsvp_limit = obj.rsvp_limit;
		self.status = obj.status;
		self.time = obj.time;
		self.updated = obj.updated;
		self.utc_offset = obj.utc_offset;
		self.visibility = obj.visibility;
		self.venue = new Venue(obj.venue);
		self.waitlist_count = obj.waitlist_count;
		self.yes_rsvp_count = obj.yes_rsvp_count;

		self.time_str = function() {
			return new Date(self.time).toString();
		};
		self.attendance = function() {
			if (self.rsvp_limit) {
				if (self.yes_rsvp_count == self.rsvp_limit)
					return "Full!"
				else
					return self.yes_rsvp_count + "/"+ self.rsvp_limit;
			} else {
				return self.yes_rsvp_count;
			}
		};
	}

	return {
		Venue: Venue,
		Event: Event
	}
});