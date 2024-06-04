use App\GraphQL\TypeRegistry;
use GraphQL\GraphQL;
use Illuminate\Http\Request;

Route::post('/graphql', function (Request $request) {
    $schema = TypeRegistry::createSchema();
    $query = $request->input('query');

    return GraphQL::executeQuery($schema, $query);
});
