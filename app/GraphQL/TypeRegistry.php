namespace App\GraphQL;

use GraphQL\Type\Definition\ObjectType;
use GraphQL\Type\Definition\Type;
use GraphQL\Type\Schema;

class TypeRegistry
{
    public static function createSchema(): Schema
    {
        $queryType = new ObjectType([
            'name' => 'Query',
            'fields' => [
                'products' => [
                    'type' => Type::listOf(Type::string()),
                    'resolve' => function () {
                        return \App\Models\Product::all();
                    },
                ],
            ],
        ]);

        return new Schema([
            'query' => $queryType,
        ]);
    }
}
