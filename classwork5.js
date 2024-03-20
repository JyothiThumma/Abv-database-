//use sample_training
db.zips.aggregate({})

//Sort.js
db.zips.aggregate([
  {
    $sort: {
      pop: -1
     }
}
//outinprojection
db.zips.aggregate([
    {
      $group: {
        _id: "$state",
        total_pop: { $sum: "$pop" }
      }
    },
    {
      $match: {
        total_pop: { $lt: 1000000 }
      }
    }
])
  [
    { _id: 'WY', total_pop: 453588},
    { _id: 'DC', total_pop: 606900},
    { _id: 'DE', total_pop: 666168},
    { _id: 'VT', total_pop: 562758},
    { _id: 'SD', total_pop: 696004},
    { _id: 'MT', total_pop: 799065},
    { _id: 'AK', total_pop: 550043},
    { _id: 'ND', total_pop: 638800}
  ]
db.zips.aggregate([
  {
		$group:{
					_id: "$state",
					total_pop: { $sum:"$pop"}
        }
  },
  {
		$match: {
				totla_pop:{$lt:1000000}
			}
		},
  {
			$out: "small_states"
}
]
)
//project.js
db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	_id:0
  }
}
])
//set.js
db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	pop_2022: { $round: { $multiply: [1.0031, "$pop"]}},
	_id:0
}
}
])
//count.js

db.zips.aggregate([
{ $count: "total_zips"}

])