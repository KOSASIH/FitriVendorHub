const Rating = require('../public/javascripts/rating');

describe('RatingController', () => {
  let ratingController;
  let ratingElement;

  beforeEach(() => {
    ratingElement = document.createElement('div');
    ratingController = new RatingController(ratingElement);
  });

  it('should set and display the rating', () => {
    ratingController.setRating(3);
    expect(ratingElement.innerHTML).toEqual('Rating: 3/5');
  });

  it('should update the display when the rating changes', () => {
    ratingController.setRating(3);
    ratingController.setRating(4);
    expect(ratingElement.innerHTML).toEqual('Rating: 4/5');
  });
});
